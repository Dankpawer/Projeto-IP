from app.schemas.models import Scenario, GeolocationResponse, GeolocationData

MOCK_SCENARIOS = {
    "demo-001": Scenario(
        scenario_id="demo-001",
        profile="Pessoa fictícia",
        sources=[
            {"type": "public_post", "content": "Exemplo inventado para a simulação: 'Adoro essa cafeteria nova no centro!'"},
            {"type": "photo_metadata", "content": "Metadado extraído: Praça Central, 14:00 (Fictício)"}
        ],
        conclusion={
            "text": "Duas publicações podem estar relacionadas, revelando uma rotina geográfica.",
            "confidence": "low",
            "limitations": [
                "Os dados não confirmam a identidade de uma pessoa real",
                "Demonstração apenas educativa"
            ]
        }
    )
}

def get_all_scenarios():
    return list(MOCK_SCENARIOS.values())

def get_scenario_by_id(scenario_id: str):
    return MOCK_SCENARIOS.get(scenario_id)

def mock_ip_lookup(ip: str):
    return GeolocationResponse(
        status="success",
        source="simulated_mock_provider",
        data=GeolocationData(
            city="Cidade Demonstrativa",
            region="Região Demonstrativa",
            country="País Demonstrativo"
        ),
        accuracy="approximate",
        stored=False
    )
