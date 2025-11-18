# asb_validator.py — ASB v1.0 validator v0.1 (18 Nov 2025)
# pip install jsonschema requests

import json
import jsonschema
from datetime import datetime

ASB_SCHEMA_V1 = {
    "type": "object",
    "required": [
        "asb_version",
        "model_id",
        "total_training_kgco2eq",
        "inference_gco2eq_per_1k_tokens"
    ],
    "properties": {
        "asb_version": {"const": "1.0"},
        "model_id": {"type": "string"},
        "total_training_kgco2eq": {"type": "number", "minimum": 0},
        "inference_gco2eq_per_1k_tokens": {"type": "number", "minimum": 0},
        "water_withdrawn_litres": {"type": "number", "minimum": 0},
        "tokens_per_joule": {"type": "number", "minimum": 0},
        "measurement": {"type": "object"}
    }
}

def validate_asb(json_data_or_path):
    """Validate a JSON file or dict against ASB v1.0 schema"""
    if isinstance(json_data_or_path, str):
        with open(json_data_or_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = json_data_or_path

    jsonschema.validate(instance=data, schema=ASB_SCHEMA_V1)
    print(f"ASB v1.0 validation PASSED for {data.get('model_id', 'unknown model')}")
    print(f"Verified on {datetime.now().strftime('%Y-%m-%d')}")
    return True

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        validate_asb(sys.argv[1])
    else:
        print("Usage: python asb_validator.py <path-to-asb-json>")
