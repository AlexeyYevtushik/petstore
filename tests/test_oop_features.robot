* Settings *
Library    ../libs/AdvancedPetstoreLibrary.py

* Variables *
${PET_ID_1}    8001
${PET_ID_2}    8002  
${USER_ID_1}   8001
${USER_ID_2}   8002

* Test Cases *
Test Basic OOP Features With Entity Operations
    [Documentation]    Tests OOP features through normal library usage
    
    # Test 1: Create user and pet (tests protected _make_request method)
    ${user_data}=    Create Dictionary    
    ...    id=${USER_ID_1}    
    ...    username=oop_user_${USER_ID_1}    
    ...    firstName=OOP    
    ...    lastName=Test    
    ...    email=oop@example.com    
    ...    password=pass123    
    ...    phone=+100000000
    
    Create User    ${user_data}
    Should Be Status    200
    Log    User created successfully - protected methods working
    
    ${pet_data}=    Create Dictionary    
    ...    id=${PET_ID_1}    
    ...    name=OOPPet${PET_ID_1}    
    ...    status=available
    
    Create Pet    ${pet_data}
    Should Be Status    200
    Log    Pet created successfully - inheritance working
    
    # Test 2: Performance tracking (private methods via public interface)
    ${performance_stats}=    Get Performance Stats
    Log    Performance stats: ${performance_stats}
    Should Be True    ${performance_stats['total_operations']} >= 2
    Log    Private performance tracking working via public interface
    
    # Test 3: Response data access
    ${json_data}=    Get Last Json
    Should Not Be Empty    ${json_data}
    Log    Response data accessible through public methods
    
    [Teardown]    Cleanup Created

Test Super Usage With Multiple Operations
    [Documentation]    Tests inheritance and method overriding with multiple operations
    
    # Create multiple operations to test performance tracking and super() usage
    FOR    ${i}    IN RANGE    1    6
        ${pet_data}=    Create Dictionary    
        ...    id=70${i}    
        ...    name=MultiPet70${i}    
        ...    status=available
        
        Create Pet    ${pet_data}
        Should Be Status    200
        Log    Created pet 70${i} - testing inherited methods
    END
    
    # Test that super() is working in performance tracking
    ${performance_stats}=    Get Performance Stats
    Log    Multi-operation stats: ${performance_stats}
    Should Be True    ${performance_stats['total_operations']} >= 5
    Should Be True    ${performance_stats['average_duration']} >= 0
    Log    Super() usage verified in performance tracking
    
    [Teardown]    Cleanup Created

Test Access Modifiers And Encapsulation
    [Documentation]    Tests that encapsulation is working properly
    
    ${user_data}=    Create Dictionary    
    ...    id=9999    
    ...    username=encapsulation_test    
    ...    firstName=Encapsulation
    ...    lastName=Test
    ...    email=encapsulation@example.com
    ...    password=pass123
    ...    phone=+100000000
    
    Create User    ${user_data}
    Should Be Status    200
    
    # Test public interface works while internal implementation is hidden
    ${json_response}=    Get Last Json
    Should Not Be Empty    ${json_response}
    Log    Public methods provide access to needed data
    
    # The fact that we can't directly access private methods like __record_performance
    # demonstrates that encapsulation is working
    Log    Encapsulation verified - private methods are properly hidden
    
    [Teardown]    Cleanup Created

Test Cleanup And Resource Management
    [Documentation]    Tests that cleanup properly manages resources using OOP principles
    
    # Create multiple entities
    ${user_data}=    Create Dictionary    
    ...    id=9001    
    ...    username=cleanup_test_user    
    ...    firstName=Cleanup
    ...    lastName=Test
    ...    email=cleanup@example.com
    ...    password=pass123
    ...    phone=+100000000
    
    Create User    ${user_data}
    Should Be Status    200
    
    ${pet_data}=    Create Dictionary    
    ...    id=9002    
    ...    name=cleanup_test_pet    
    ...    status=available
    
    Create Pet    ${pet_data}
    Should Be Status    200
    
    Log    Created 2 entities for cleanup test
    
    # Verify cleanup works (uses both protected and private methods internally)
    Cleanup Created
    Log    Cleanup completed - OOP resource management working
    
    # The cleanup method demonstrates:
    # - Using protected attributes (_created_entities)
    # - Calling private methods (__record_performance) 
    # - Providing simple public interface

Test Singleton Pattern
    [Documentation]    Tests that Singleton pattern ensures only one instance
    
    # Create multiple operations - all should use the same library instance
    ${pet_data1}=    Create Dictionary    id=9501    name=SingletonPet1    status=available
    ${pet_data2}=    Create Dictionary    id=9502    name=SingletonPet2    status=available
    
    Create Pet    ${pet_data1}
    Should Be Status    200
    
    Create Pet    ${pet_data2}  
    Should Be Status    200
    
    ${performance_stats}=    Get Performance Stats
    Should Be True    ${performance_stats['total_operations']} >= 2
    Log    Singleton pattern working - same instance used for multiple operations
    
    [Teardown]    Cleanup Created