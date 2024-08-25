import wandb

with wandb.init() as run:
    run.log({"hello": "world"})
