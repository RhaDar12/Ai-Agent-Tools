from pathlib import Path

from faster_whisper import WhisperModel

from core import (
    DIRS,
    ensure_dirs,
    make_id,
    save_json,
    success_response,
    error_response
)


DEFAULT_MODEL = "base"


def transcribe_audio(file_path, model_size=DEFAULT_MODEL, language="id"):
    """
    Mengubah audio menjadi teks menggunakan faster-whisper.
    Output transkrip disimpan sebagai .txt dan .json.
    """

    tool_name = "transcribe_audio"

    try:
        ensure_dirs()

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File audio tidak ditemukan: {file_path}")

        transcript_id = make_id("stt")

        txt_path = DIRS["documents"] / f"{transcript_id}.txt"
        json_path = DIRS["documents"] / f"{transcript_id}.json"

        model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

        segments, info = model.transcribe(
            str(file_path),
            language=language,
            vad_filter=True
        )

        full_text_parts = []
        segment_list = []

        for segment in segments:
            text = segment.text.strip()
            full_text_parts.append(text)

            segment_list.append({
                "start": segment.start,
                "end": segment.end,
                "text": text
            })

        full_text = " ".join(full_text_parts).strip()

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(full_text)

        result_data = {
            "source_file": str(file_path),
            "model_size": model_size,
            "language": language,
            "detected_language": info.language,
            "language_probability": info.language_probability,
            "text": full_text,
            "segments": segment_list,
            "txt_path": str(txt_path),
            "json_path": str(json_path)
        }

        save_json(json_path, result_data)

        return success_response(
            tool=tool_name,
            message="Audio berhasil diubah menjadi teks",
            file_path=txt_path,
            extra={
                "source_file": str(file_path),
                "transcript_id": transcript_id,
                "text": full_text,
                "txt_path": str(txt_path),
                "json_path": str(json_path),
                "model_size": model_size,
                "language": language
            }
        )

    except Exception as e:
        return error_response(tool_name, e)