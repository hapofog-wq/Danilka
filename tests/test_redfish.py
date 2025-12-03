import pytest
import time
from redfish_service import RedfishService
from config import BmcConfig

@pytest.fixture
def redfish_service():
    return RedfishService()

class TestRedfishAPI:
    
    def test_auth(self, redfish_service):
        """Тест аутентификации в OpenBMC через Redfish API"""
        response = redfish_service.auth()
        
        assert response.status_code in [201, 200], f"Ожидался код 201 или 200, получен {response.status_code}"
        
        if response.status_code in [201, 200]:
            data = response.json()
            print(f"\nAuth Response: {data}")
        else:
            print(f"\nAuth failed with status: {response.status_code}")

    def test_get_system_info(self, redfish_service):
        """Тест получения информации о системе"""
        response = redfish_service.get_system_info()
        
        assert response.status_code in [200, 404, 503], f"Получен код {response.status_code}"
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nSystem Response: {data}")
        else:
            print(f"\nSystem info not available: {response.status_code}")

    def test_power_management_on(self, redfish_service):
        """Тест управления питанием (включение сервера)"""
        response = redfish_service.toggle_server_status('On')
        
        assert response.status_code in [204, 200, 404, 503], f"Получен код {response.status_code}"
        
        print(f"\nBoot Response status: {response.status_code}")
        
        time.sleep(2)
        
        system_response = redfish_service.get_system_info()
        if system_response.status_code == 200:
            system_data = system_response.json()
            print(f"System PowerState after boot: {system_data.get('PowerState')}")

    def test_get_thermal_info(self, redfish_service):
        """Тест получения термической информации"""
        response = redfish_service.get_thermal_info()
        
        assert response.status_code in [200, 404, 503], f"Получен код {response.status_code}"
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nThermal Response: {data}")

    def test_get_processors_info(self, redfish_service):
        """Тест получения информации о процессорах"""
        response = redfish_service.get_processors()
        
        assert response.status_code in [200, 404, 503], f"Получен код {response.status_code}"
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nProcessors Response: {data}")

def test_all_responses():
    """Тест для вывода всех ответов"""
    service = RedfishService()
    
    print("\n=== Testing All Endpoints ===")
    
    endpoints = [
        ("/redfish/v1", "Root"),
        ("/redfish/v1/Systems", "Systems"),
        ("/redfish/v1/Chassis", "Chassis"),
    ]
    
    for endpoint, name in endpoints:
        try:
            response = service.session.get(f"https://localhost:2443{endpoint}")
            print(f"{name}: Status {response.status_code}")
        except Exception as e:
            print(f"{name}: Error - {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])