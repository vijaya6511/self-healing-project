from engine.dom_capture import capture_dom
from engine.dom_parser import extract_elements
from engine.ai_engine import find_best_match
from engine.locator_generator import generate_locator

def heal_locator(page, old_locator_info, action_type="click", value=None,best_score=0):

    print("Starting healing process")

    html = capture_dom(page)

    tag = "button" if action_type == "click" else "input"

    candidates = extract_elements(html, tag)

    old_element = {
        "id": old_locator_info["value"],
        "class": "",
        "text": "",
        "tag": tag
    }

    best_match, score = find_best_match(old_element, candidates)

    print(f"Best match found with score: {score}")

    new_by, new_value = generate_locator(best_match)

    print(f"New locator: {new_by} = {new_value}")

    # Convert to Playwright selector
    if new_by == "id":
        selector = f"#{new_value}"
    elif new_by == "css":
        selector = new_value
    elif new_by == "xpath":
        selector = f"xpath={new_value}"
    else:
        selector = new_value

    # Retry action
    if action_type == "click":
        page.click(selector)
    elif action_type == "fill":
        page.fill(selector, value)

    print("Healing successful")

    return {"by": new_by, "value": new_value}
#     return {
#     "by": "id",
#     "value": best_match,
#     "score": round(best_score, 3)
# }