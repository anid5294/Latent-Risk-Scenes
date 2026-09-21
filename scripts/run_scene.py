"""Load a latent-risk scene and verify that the environment steps."""

import argparse
import os
import sys
import tempfile
from pathlib import Path


DEFAULT_SCENE = "KITCHEN_SCENE3_turn_on_the_stove_and_put_the_book_on_it.bddl"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--libero-root", type=Path, required=True)
    parser.add_argument("--scene", default=DEFAULT_SCENE)
    parser.add_argument("--steps", type=int, default=10)
    args = parser.parse_args()

    libero_root = args.libero_root.expanduser().resolve()
    scene = (
        libero_root
        / "libero/libero/bddl_files/libero_risk"
        / Path(args.scene).name
    )
    if not scene.is_file():
        raise SystemExit(f"Scene not installed: {scene}")

    with tempfile.TemporaryDirectory(prefix="libero-risk-") as config_dir:
        config_path = Path(config_dir) / "config.yaml"
        config_path.write_text(
            "\n".join(
                [
                    f"assets: {libero_root / 'libero/libero/assets'}",
                    f"bddl_files: {libero_root / 'libero/libero/bddl_files'}",
                    f"benchmark_root: {libero_root / 'libero/libero'}",
                    f"datasets: {libero_root / 'libero/datasets'}",
                    f"init_states: {libero_root / 'libero/libero/init_files'}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        os.environ["LIBERO_CONFIG_PATH"] = config_dir
        sys.path.insert(0, str(libero_root))

        from libero.libero.envs.env_wrapper import ControlEnv

        env = ControlEnv(
            bddl_file_name=str(scene),
            use_camera_obs=False,
            has_renderer=False,
            has_offscreen_renderer=False,
        )
        try:
            env.reset()
            for _ in range(args.steps):
                env.step([0.0] * 7)
            print(f"Loaded: {scene.name}")
            print(f"Goal satisfied after initialization: {env.check_success()}")
        finally:
            env.close()


if __name__ == "__main__":
    main()
