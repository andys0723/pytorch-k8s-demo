# distributed_demo.py
import os
import time
import torch
import torch.distributed as dist
import torch.multiprocessing as mp

def setup(rank, world_size):
    # Initialize the process group
    dist.init_process_group(
        backend="gloo",  # 'nccl' for GPU, 'gloo' works on CPU
        init_method=f"tcp://{os.environ['MASTER_ADDR']}:{os.environ['MASTER_PORT']}",
        rank=rank,
        world_size=world_size,
    )

def cleanup():
    dist.destroy_process_group()

def worker(rank, world_size):
    setup(rank, world_size)

    # Create a tensor on CPU (use device='cuda' for GPU)
    tensor = torch.ones(2, 2) * (rank + 1)
    print(f"[Rank {rank}] Tensor before all_reduce:\n{tensor}")

    # Long-lived demo loop
    for step in range(5):
        dist.all_reduce(tensor, op=dist.ReduceOp.SUM)
        print(f"[Rank {rank}] Tensor after all_reduce step {step}:\n{tensor}")
        time.sleep(5)  # wait a bit to simulate work

    print(f"[Rank {rank}] Worker done.")
    cleanup()

def main():
    world_size = int(os.environ.get("WORLD_SIZE", 2))
    rank = int(os.environ.get("RANK", 0))

    print(f"Starting process rank {rank} out of {world_size} total.")

    # Run single-process per pod (or per container)
    worker(rank, world_size)

    # Keep master alive if rank 0
    if rank == 0:
        print("Master process alive, waiting for workers...")
        while True:
            time.sleep(60)

if __name__ == "__main__":
    main()
