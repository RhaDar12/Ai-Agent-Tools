from core import ensure_dirs, success_response, error_response, log_info

ensure_dirs()

log_info("test_core", "Core berhasil dijalankan")

print(success_response(
    tool="test_core",
    message="Core berhasil dites"
))

print(error_response(
    tool="test_core",
    error="Ini contoh error test"
))