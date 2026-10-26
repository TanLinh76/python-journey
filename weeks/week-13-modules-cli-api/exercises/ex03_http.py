"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import build_get_request, parse_json_response


fixture = b'{"lesson": 13}'


def main() -> None:
    """Check request structure, successful JSON, and failure paths."""
    request = build_get_request("https://example.invalid/lesson")
    assert request.method == "GET"
    assert request.full_url == "https://example.invalid/lesson"

    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13
    print("Successful response:", data)

    try:
        parse_json_response(500, b'{"error": "server error"}')
    except ValueError as error:
        print("Expected status error:", error)
    else:
        raise AssertionError("HTTP 500 response should have been rejected")

    try:
        parse_json_response(200, b"not-json")
    except ValueError as error:
        print("Expected JSON error:", error)
    else:
        raise AssertionError("Malformed JSON should have been rejected")


if __name__ == "__main__":
    main()
