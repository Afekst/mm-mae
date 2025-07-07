# src/mm_mae/train.py
import hydra
import pytorch_lightning as pl
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="../../configs/train", config_name="default")
def main(cfg: DictConfig):
    pl.seed_everything(cfg.seed)
    # TODO: replace with real datamodule & model
    print("Config looks good:", cfg)


if __name__ == "__main__":
    main()
