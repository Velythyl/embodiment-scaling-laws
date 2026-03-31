# Data Transfer Guide: Mila → Alliance Canada (Fir)

Transfer ~4TB of logs from this cluster to `fir.alliancecan.ca`.

## Prerequisites

- Private key: `./ccdb` (already in workspace)
- Destination: `cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws`

## Quick Start

### 1. Test SSH Connection

```bash
eval `ssh-agent -s`
ssh-add ccdb
ssh -i ./ccdb cgauthie@fir.alliancecan.ca "echo 'Connection successful'"
```

### 2 run

```
find /network/scratch/c/charlie.gauthier/embodiment-scaling-laws/logs/rsl_rl -mindepth 1 -maxdepth 1 -print0 | xargs -0 -P8 -I% rsync -az --partial  % cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/ 2>&1
```

### 3 run single ssh (avoids multiple 2FA prompts)

Use SSH connection multiplexing to authenticate once, then reuse that connection for all parallel rsync processes:

```bash
# 1. Start master connection (authenticate with 2FA once)
ssh -fNM -S /tmp/ssh-fir -i ./ccdb cgauthie@fir.alliancecan.ca

# 2. Run parallel rsync using that socket (no more 2FA prompts)
find /network/scratch/c/charlie.gauthier/embodiment-scaling-laws/logs/rsl_rl -mindepth 1 -maxdepth 1 -print0 | xargs -0 -P1 -I% rsync -az --partial -e 'ssh -S /tmp/ssh-fir' % cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/rsl_rl 2>&1

# 3. When done, close the master connection
ssh -S /tmp/ssh-fir -O exit cgauthie@fir.alliancecan.ca
```

**Flags explained:**
- `-f` — background after auth
- `-N` — no remote command (just hold the connection)
- `-M` — master mode (create the control socket)
- `-S /tmp/ssh-fir` — path to the control socket



---- IGNORe



### 2. Submit as SLURM Job (Recommended)

Run the transfer on a compute node with internet access:

```bash
sbatch --partition=unkillable-cpu \
    --time=2-00:00:00 \
    --cpus-per-task=2 \
    --mem=16G \
    --job-name=transfer-logs \
    --output=transfer-%j.log \
    --wrap="rsync -avz --info=progress2 --partial -e 'ssh -i $(pwd)/ccdb_nopass' $(pwd)/logs/ cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/"
```

**Parallel transfer (8 processes, faster for many subdirectories):**

```bash
sbatch --partition=unkillable-cpu \
    --time=2-00:00:00 \
    --cpus-per-task=2 \
    --mem=16G \
    --job-name=transfer-logs-parallel \
    --output=transfer-%j.log \
    --error=transfer-%j.log \
    --wrap="find /network/scratch/c/charlie.gauthier/embodiment-scaling-laws/logs/rsl_rl -mindepth 1 -maxdepth 1 -print0 | xargs -0 -P8 -I% rsync -az --partial -e 'ssh -i /network/scratch/c/charlie.gauthier/embodiment-scaling-laws/ccdb -o IdentitiesOnly=yes -o PreferredAuthentications=publickey -o BatchMode=yes' % cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/ 2>&1"
```

This launches 8 parallel rsync processes, each handling a top-level subdirectory of `logs/`. Good for I/O-bound transfers with many subdirectories.

Monitor the job:
```bash
# Check job status
squeue -u $USER

# Watch the transfer log (once job starts)
tail -f transfer-*.log
```

**Note**: If interrupted, resubmit the same command - rsync will resume where it left off.

### 3. Alternative: Start a Screen Session

This ensures the transfer survives SSH disconnections:

```bash
screen -S transfer
```

- **Detach**: `Ctrl+A`, then `D`
- **Reattach**: `screen -r transfer`
- **List sessions**: `screen -ls`

### 3. Run the Transfer

```bash
rsync -avz --info=progress2 --partial -e "ssh -i ./ccdb" \
    ./logs/ \
    cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/
```

## Command Options Explained

| Option | Purpose |
|--------|---------|
| `-a` | Archive mode (preserves permissions, timestamps, symlinks) |
| `-v` | Verbose output |
| `-z` | Compress during transfer (no local disk space needed) |
| `--info=progress2` | Show overall progress (better for many small files) |
| `--partial` | Keep partially transferred files for resume |
| `-e "ssh -i ./ccdb"` | Use the specified private key |

## Resuming After Interruption

Simply re-run the same rsync command. It will:
- Skip files that are already fully transferred
- Resume partially transferred files
- Only transfer new/changed files

```bash
# Just run the same command again
rsync -avz --info=progress2 --partial -e "ssh -i ./ccdb" \
    ./logs/ \
    cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/
```

## Alternative: Dry Run (Preview)

To see what would be transferred without actually transferring:

```bash
rsync -avzn --info=progress2 -e "ssh -i ./ccdb" \
    ./logs/ \
    cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/
```

(Note the `-n` flag for dry-run)

## Troubleshooting

### Permission denied (publickey)
```bash
chmod 600 ./ccdb
```

### Connection timeout
Add SSH options to improve stability:
```bash
rsync -avz --info=progress2 --partial \
    -e "ssh -i ./ccdb -o ServerAliveInterval=60 -o ServerAliveCountMax=3" \
    ./logs/ \
    cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/
```

### Transfer is slow
For many small files, consider using `--compress-level=1` for faster (lighter) compression:
```bash
rsync -avz --compress-level=1 --info=progress2 --partial -e "ssh -i ./ccdb" \
    ./logs/ \
    cgauthie@fir.alliancecan.ca:/scratch/cgauthie/embodiment-scaling-laws/logs/
```

## Verifying the Transfer

After completion, verify file counts match:

```bash
# Local count
find ./logs -type f | wc -l

# Remote count
ssh -i ./ccdb cgauthie@fir.alliancecan.ca "find /scratch/cgauthie/embodiment-scaling-laws/logs -type f | wc -l"
```

## Estimated Time

For ~4TB of small files over a typical inter-cluster connection:
- Expect several hours to a few days depending on network conditions
- The `--info=progress2` flag will show estimated remaining time
