from pathlib import Path

from core import (
    ensure_dirs,
    success_response,
    error_response
)

from comfy_image_tool import (
    generate_comfy_image,
    generate_comfy_img2img,
    generate_comfy_upscale
)

from bg_remove_tool import remove_background

from send_file_whatsapp import send_file_whatsapp


def generate_asset_pipeline(
    prompt,
    negative_prompt="blurry, low quality, distorted, watermark, text, bad anatomy",
    target=None,
    caption="Asset dari AI-Agent",
    do_upscale=False,
    do_remove_bg=False,
    send_to_whatsapp=False
):
    """
    Pipeline:
    txt2img -> optional upscale -> optional remove background -> optional send WhatsApp
    """

    tool_name = "generate_asset_pipeline"

    try:
        ensure_dirs()

        if not prompt or not prompt.strip():
            raise ValueError("Prompt kosong, tidak bisa membuat asset.")

        steps = []

        # 1. Generate image
        gen_result = generate_comfy_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=1024,
            height=1024,
            steps=6,
            cfg=2,
            sampler_name="euler",
            scheduler="karras",
            seed=-1,
            target=target,
            caption=caption
        )

        steps.append({
            "step": "txt2img",
            "result": gen_result
        })

        if not gen_result.get("success"):
            return error_response(tool_name, gen_result.get("error", "Generate image gagal"))

        current_file = gen_result.get("file_path")
        current_delivery_id = gen_result.get("delivery_id")

        if not current_file:
            raise RuntimeError("Generate image berhasil tapi file_path kosong.")

        # 2. Optional upscale
        if do_upscale:
            upscale_result = generate_comfy_upscale(
                image_path=current_file,
                target=target,
                caption=f"{caption} - Upscaled"
            )

            steps.append({
                "step": "upscale",
                "result": upscale_result
            })

            if not upscale_result.get("success"):
                return error_response(tool_name, upscale_result.get("error", "Upscale gagal"))

            current_file = upscale_result.get("file_path")
            current_delivery_id = upscale_result.get("delivery_id")

        # 3. Optional remove background
        if do_remove_bg:
            bg_result = remove_background(
                image_path=current_file,
                target=target,
                caption=f"{caption} - Tanpa background"
            )

            steps.append({
                "step": "remove_background",
                "result": bg_result
            })

            if not bg_result.get("success"):
                return error_response(tool_name, bg_result.get("error", "Remove background gagal"))

            current_file = bg_result.get("file_path")
            current_delivery_id = bg_result.get("delivery_id")

        # 4. Optional send to WhatsApp
        send_result = None

        if send_to_whatsapp:
            if not target:
                raise ValueError("Target WhatsApp kosong, tidak bisa mengirim hasil pipeline.")

            send_result = send_file_whatsapp(
                file_path=current_file,
                target=target,
                caption=caption,
                delivery_id=current_delivery_id
            )

            steps.append({
                "step": "send_whatsapp",
                "result": send_result
            })

            if not send_result.get("success"):
                return error_response(tool_name, send_result.get("error", "Kirim WhatsApp gagal"))

        return success_response(
            tool=tool_name,
            message="Pipeline asset berhasil dijalankan",
            file_path=current_file,
            extra={
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "do_upscale": do_upscale,
                "do_remove_bg": do_remove_bg,
                "send_to_whatsapp": send_to_whatsapp,
                "target": target,
                "caption": caption,
                "final_file_path": current_file,
                "delivery_id": current_delivery_id,
                "steps": steps,
                "send_result": send_result
            }
        )

    except Exception as e:
        return error_response(tool_name, e)


def img2img_asset_pipeline(
    image_path,
    prompt,
    negative_prompt="blurry, low quality, distorted, watermark, text, bad anatomy",
    target=None,
    caption="Asset img2img dari AI-Agent",
    denoise=0.6,
    do_upscale=False,
    do_remove_bg=False,
    send_to_whatsapp=False
):
    """
    Pipeline:
    img2img -> optional upscale -> optional remove background -> optional send WhatsApp
    """

    tool_name = "img2img_asset_pipeline"

    try:
        ensure_dirs()

        if not image_path or not str(image_path).strip():
            raise ValueError("Image path kosong.")

        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image input tidak ditemukan: {image_path}")

        if not prompt or not prompt.strip():
            raise ValueError("Prompt kosong, tidak bisa menjalankan img2img pipeline.")

        steps = []

        # 1. Img2img
        img2img_result = generate_comfy_img2img(
            image_path=image_path,
            prompt=prompt,
            negative_prompt=negative_prompt,
            steps=6,
            cfg=1.5,
            sampler_name="euler",
            scheduler="karras",
            denoise=denoise,
            seed=-1,
            target=target,
            caption=caption
        )

        steps.append({
            "step": "img2img",
            "result": img2img_result
        })

        if not img2img_result.get("success"):
            return error_response(tool_name, img2img_result.get("error", "Img2img gagal"))

        current_file = img2img_result.get("file_path")
        current_delivery_id = img2img_result.get("delivery_id")

        if not current_file:
            raise RuntimeError("Img2img berhasil tapi file_path kosong.")

        # 2. Optional upscale
        if do_upscale:
            upscale_result = generate_comfy_upscale(
                image_path=current_file,
                target=target,
                caption=f"{caption} - Upscaled"
            )

            steps.append({
                "step": "upscale",
                "result": upscale_result
            })

            if not upscale_result.get("success"):
                return error_response(tool_name, upscale_result.get("error", "Upscale gagal"))

            current_file = upscale_result.get("file_path")
            current_delivery_id = upscale_result.get("delivery_id")

        # 3. Optional remove background
        if do_remove_bg:
            bg_result = remove_background(
                image_path=current_file,
                target=target,
                caption=f"{caption} - Tanpa background"
            )

            steps.append({
                "step": "remove_background",
                "result": bg_result
            })

            if not bg_result.get("success"):
                return error_response(tool_name, bg_result.get("error", "Remove background gagal"))

            current_file = bg_result.get("file_path")
            current_delivery_id = bg_result.get("delivery_id")

        # 4. Optional send WhatsApp
        send_result = None

        if send_to_whatsapp:
            if not target:
                raise ValueError("Target WhatsApp kosong, tidak bisa mengirim hasil pipeline.")

            send_result = send_file_whatsapp(
                file_path=current_file,
                target=target,
                caption=caption,
                delivery_id=current_delivery_id
            )

            steps.append({
                "step": "send_whatsapp",
                "result": send_result
            })

            if not send_result.get("success"):
                return error_response(tool_name, send_result.get("error", "Kirim WhatsApp gagal"))

        return success_response(
            tool=tool_name,
            message="Pipeline img2img asset berhasil dijalankan",
            file_path=current_file,
            extra={
                "source_image_path": image_path,
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "denoise": denoise,
                "do_upscale": do_upscale,
                "do_remove_bg": do_remove_bg,
                "send_to_whatsapp": send_to_whatsapp,
                "target": target,
                "caption": caption,
                "final_file_path": current_file,
                "delivery_id": current_delivery_id,
                "steps": steps,
                "send_result": send_result
            }
        )

    except Exception as e:
        return error_response(tool_name, e)