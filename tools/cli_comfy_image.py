import json
import sys

from comfy_image_tool import (
    check_comfyui,
    generate_comfy_image,
    generate_comfy_img2img,
    generate_comfy_upscale
)


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_comfy_image.py <check|txt2img|img2img|upscale> ...'
            )

        action = sys.argv[1]

        if action == "check":
            result = check_comfyui()

        elif action == "txt2img":
            if len(sys.argv) < 3:
                raise ValueError(
                    'Format: py cli_comfy_image.py txt2img "<prompt>" [negative_prompt] [width] [height] [steps] [cfg] [sampler] [scheduler] [seed] [workflow_path] [target] [caption]'
                )

            prompt = sys.argv[2]
            negative_prompt = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "low quality, blurry, distorted, watermark, text"
            width = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
            height = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
            steps = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] else None
            cfg = sys.argv[7] if len(sys.argv) > 7 and sys.argv[7] else None
            sampler = sys.argv[8] if len(sys.argv) > 8 and sys.argv[8] else None
            scheduler = sys.argv[9] if len(sys.argv) > 9 and sys.argv[9] else None
            seed = sys.argv[10] if len(sys.argv) > 10 and sys.argv[10] else None
            workflow_path = sys.argv[11] if len(sys.argv) > 11 and sys.argv[11] else None
            target = sys.argv[12] if len(sys.argv) > 12 and sys.argv[12] else None
            caption = sys.argv[13] if len(sys.argv) > 13 and sys.argv[13] else "Gambar dari ComfyUI AI-Agent"

            result = generate_comfy_image(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                steps=steps,
                cfg=cfg,
                sampler_name=sampler,
                scheduler=scheduler,
                seed=seed,
                workflow_path=workflow_path,
                target=target,
                caption=caption
            )

        elif action == "img2img":
            if len(sys.argv) < 4:
                raise ValueError(
                    'Format: py cli_comfy_image.py img2img "<image_path>" "<prompt>" [negative_prompt] [steps] [cfg] [sampler] [scheduler] [denoise] [seed] [workflow_path] [target] [caption]'
                )

            image_path = sys.argv[2]
            prompt = sys.argv[3]
            negative_prompt = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else "low quality, blurry, distorted, watermark, text"
            steps = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
            cfg = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] else None
            sampler = sys.argv[7] if len(sys.argv) > 7 and sys.argv[7] else None
            scheduler = sys.argv[8] if len(sys.argv) > 8 and sys.argv[8] else None
            denoise = sys.argv[9] if len(sys.argv) > 9 and sys.argv[9] else 0.6
            seed = sys.argv[10] if len(sys.argv) > 10 and sys.argv[10] else None
            workflow_path = sys.argv[11] if len(sys.argv) > 11 and sys.argv[11] else None
            target = sys.argv[12] if len(sys.argv) > 12 and sys.argv[12] else None
            caption = sys.argv[13] if len(sys.argv) > 13 and sys.argv[13] else "Gambar img2img dari ComfyUI AI-Agent"

            result = generate_comfy_img2img(
                image_path=image_path,
                prompt=prompt,
                negative_prompt=negative_prompt,
                steps=steps,
                cfg=cfg,
                sampler_name=sampler,
                scheduler=scheduler,
                denoise=denoise,
                seed=seed,
                workflow_path=workflow_path,
                target=target,
                caption=caption
            )

        elif action == "upscale":
            if len(sys.argv) < 3:
                raise ValueError(
                    'Format: py cli_comfy_image.py upscale "<image_path>" [upscale_model] [workflow_path] [target] [caption]'
                )

            image_path = sys.argv[2]
            upscale_model = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None
            workflow_path = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
            target = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
            caption = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] else "Gambar upscale dari ComfyUI AI-Agent"

            result = generate_comfy_upscale(
                image_path=image_path,
                upscale_model=upscale_model,
                workflow_path=workflow_path,
                target=target,
                caption=caption
            )

        else:
            raise ValueError(f"Action tidak dikenal: {action}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_comfy_image",
            "message": "Gagal menjalankan CLI ComfyUI image",
            "file_path": None,
            "delivered_file": {
                "status": "failed",
                "sent_to": None,
                "sent_at": None,
                "delivery_id": None
            },
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()
