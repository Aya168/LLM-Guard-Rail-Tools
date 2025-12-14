from llm_guard_rail_tools import LLMGuardRailTools
import json

# Initialize the LLMGuardRailTools SDK
guard_rail = LLMGuardRailTools()

print("--- Testing valid JSON output ---")
valid_json_output = '{"name": "Alice", "age": 30, "city": "New York"}'
is_clean, processed_output = guard_rail.process_llm_output(valid_json_output)
print(f"Is clean: {is_clean}, Processed output: {processed_output}")
print("-" * 30)

print("--- Testing malformed JSON output (simulated) ---")
malformed_json_output = '{"name": "Bob", "age": 25, "city": "London",}' # Trailing comma
is_clean, processed_output = guard_rail.process_llm_output(malformed_json_output)
print(f"Is clean: {is_clean}, Processed output: {processed_output}")
print("-" * 30)

print("--- Testing plain text output ---")
plain_text_output = "This is a simple text response without any JSON."
is_clean, processed_output = guard_rail.process_llm_output(plain_text_output)
print(f"Is clean: {is_clean}, Processed output: {processed_output}")
print("-" * 30)

print("--- Testing output with potential hallucination patterns (simulated) ---")
hallucinated_output = "The capital of France is Berlin. Also, Mars is made of cheese."
is_clean, processed_output = guard_rail.process_llm_output(hallucinated_output)
print(f"Is clean: {is_clean}, Processed output: {processed_output}")
print("-" * 30)

# Example with a JSON schema (this would require a more robust JsonIntegrityAndSchemaEnforcement)
simple_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age"]
}
print("--- Testing valid JSON with schema (simulated) ---")
valid_json_output_with_schema = '{"name": "Charlie", "age": 40, "city": "Paris"}'
is_clean, processed_output = guard_rail.process_llm_output(valid_json_output_with_schema, json_schema=simple_schema)
print(f"Is clean: {is_clean}, Processed output: {processed_output}")
print("-" * 30)
