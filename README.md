OOP Concepts in Robot Framework API Testing
This project demonstrates Object-Oriented Programming principles, Magic Methods, Access Modifiers, super() usage, and Design Patterns through a practical Robot Framework API testing library for PetStore.

OOP Principles
1. Encapsulation
Hiding internal implementation while exposing public interfaces.

Code Example:

python
class AdvancedPetstoreLibrary(BaseApiLibrary):
    def __init__(self):
        super().__init__("https://petstore.swagger.io/v2")
        self.__performance_data = []  # Private attribute
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Public method to access private data"""
        if not self.__performance_data:
            return {}
        
        durations = [item['duration'] for item in self.__performance_data]
        return {
            'total_operations': len(self.__performance_data),
            'average_duration': sum(durations) / len(durations)
        }
2. Inheritance
Creating hierarchical relationships between classes.

Code Example:

python
class BaseApiLibrary(metaclass=SingletonMeta):
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._created_entities = []
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Response:
        url = f"{self._base_url}{endpoint}"
        return self.__session.request(method, url, **kwargs)

class AdvancedPetstoreLibrary(BaseApiLibrary):
    def create_pet(self, payload: dict) -> Response:
        response = self._make_request("POST", "/pet", json=payload)  # Using inherited method
        if response.status_code == 200:
            self._created_entities.append(('pet', payload['id']))  # Using inherited attribute
        return response
3. Polymorphism
Different classes can be used interchangeably.

Code Example:

python
class ResponseHandler(ABC):
    @abstractmethod
    def handle_response(self, response: Response) -> Dict[str, Any]:
        pass

class JsonResponseHandler(ResponseHandler):
    def handle_response(self, response: Response) -> Dict[str, Any]:
        return {'data': response.json(), 'content_type': 'json'}

class TextResponseHandler(ResponseHandler):
    def handle_response(self, response: Response) -> Dict[str, Any]:
        return {'data': response.text, 'content_type': 'text'}
4. Abstraction
Hiding complex implementation details.

Code Example:

python
def create_user(self, payload: dict) -> Response:
    """Simple public interface hiding complex internals"""
    response = self._make_request("POST", "/user", json=payload)
    if response.status_code == 200:
        self._created_entities.append(('user', payload['username']))
        self.__record_performance('create_user', start_time)  # Hidden internal call
    return response
Magic Methods
Container Behavior
python
def __len__(self) -> int:
    """Enables len(library_instance)"""
    return len(self._created_entities)

def __getitem__(self, index: int) -> tuple:
    """Enables library_instance[index]"""
    return self._created_entities[index]

def __iter__(self):
    """Enables for entity in library_instance"""
    return iter(self._created_entities)
String Representation
python
def __str__(self) -> str:
    """User-friendly string representation"""
    return f"{self.__class__.__name__}(entities={len(self)})"

def __repr__(self) -> str:
    """Developer-friendly representation"""
    return f"<{self.__class__.__name__} at {hex(id(self))}>"
Context Manager
python
def __enter__(self):
    """Enables 'with' statement support"""
    return self

def __exit__(self, exc_type, exc_val, exc_tb):
    """Auto cleanup when exiting 'with' block"""
    self.cleanup_created()
Access Modifiers
Public Members (No underscore)
python
def create_pet(self, payload: dict) -> Response:
    """Public method - part of external API"""
    return self._make_request("POST", "/pet", json=payload)

def should_be_status(self, expected_status: int):
    """Public method for test assertions"""
    actual_status = self._last_response.status_code
    if actual_status != expected_status:
        raise AssertionError(f"Expected {expected_status}, got {actual_status}")
Protected Members (Single underscore _)
python
def _make_request(self, method: str, endpoint: str, **kwargs) -> Response:
    """Protected method - for internal use and subclasses"""
    url = f"{self._base_url}{endpoint}"
    return self.__session.request(method, url, **kwargs)

def _store_response(self, response: Response):
    """Protected method - processes response internally"""
    self._last_response = response
    self._increment_request_count()
Private Members (Double underscore __)
python
def __record_performance(self, operation: str, start_time: datetime):
    """Private method - name mangled"""
    duration = (datetime.now() - start_time).total_seconds()
    self.__performance_data.append({
        'operation': operation,
        'duration': duration
    })

def __init__(self, base_url: str):
    self.__session = requests.Session()  # Private attribute
    self.__request_count = 0  # Private counter
 super() Usage
Constructor Chaining
python
class AdvancedPetstoreLibrary(BaseApiLibrary):
    def __init__(self):
        # Call parent constructor first
        super().__init__("https://petstore.swagger.io/v2")
        # Then initialize subclass-specific attributes
        self.__performance_data = []
 Method Extension
python
def __str__(self) -> str:
    # Get parent's string representation
    base_str = super().__str__()
    # Enhance it with subclass information
    return f"Advanced{base_str}"
 Design Patterns
1. Singleton Pattern
Ensures only one instance exists.

Code Example:

python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class BaseApiLibrary(metaclass=SingletonMeta):
    pass
2. Strategy Pattern
Interchangeable algorithms.

Code Example:

python
class ResponseHandler(ABC):
    @abstractmethod
    def handle_response(self, response: Response) -> Dict[str, Any]:
        pass

class JsonResponseHandler(ResponseHandler):
    def handle_response(self, response: Response) -> Dict[str, Any]:
        return {'data': response.json(), 'content_type': 'json'}

class TextResponseHandler(ResponseHandler):
    def handle_response(self, response: Response) -> Dict[str, Any]:
        return {'data': response.text, 'content_type': 'text'}
3. Template Method Pattern
Algorithm skeleton in base class.

Code Example:

python
class BaseApiLibrary:
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Response:
        # Template method defining algorithm structure
        url = self._build_url(endpoint)      # Common step
        response = self._send_request(method, url, **kwargs)  # Common step
        self._store_response(response)       # Common step
        return response
 Testing OOP Concepts
Robot Framework Test Examples
robot
* Settings *
Library    ../libs/AdvancedPetstoreLibrary.py

* Test Cases *
Test Inheritance And Method Overriding
    ${pet_data}=    Create Dictionary    id=7001    name=TestPet    status=available
    Create Pet    ${pet_data}
    Should Be Status    200
    # Demonstrates inheritance and method overriding

Test Encapsulation In Action
    ${user_data}=    Create Dictionary    id=8001    username=test_user
    Create User    ${user_data}
    ${stats}=    Get Performance Stats
    # Demonstrates encapsulation - private data via public method

Test Singleton Pattern
    Create Pet    ${pet1}
    Create Pet    ${pet2}
    ${stats}=    Get Performance Stats
    Should Be True    ${stats}[total_operations] == 2
    # Demonstrates Singleton - same instance tracks all operations
 Running the Tests
bash
# Install dependencies
pip install robotframework requests robotframework-requests

# Run tests
robot -d results tests/test_oop_simple.robot

# View results
open results/log.html
 Expected Output
When tests run successfully, you'll see demonstrations of:

- Encapsulation: Private data accessed through public methods

- Inheritance: Child classes extending parent functionality

- Polymorphism: Interchangeable algorithms

- Abstraction: Complex internals hidden behind simple interfaces

- Magic Methods: Container-like behavior and clean representations

- Access Control: Proper use of public/protected/private members

- Design Patterns: Singleton, Strategy, and Template Method patterns

This project shows how OOP principles create maintainable, extensible test automation frameworks while keeping test cases simple and readable.

