TMP_USER = {
    'resourceType': 'Patient',
    'id': '98736458',
    'identifier': [{
        'type': {
            'coding': {
                'system': 'http://hl7.org/fhir/vs/identifier-type',
                'code': 'MR'
            },
            'text': 'Medical Record'
        },
        'system': 'http://hl7.org/fhir/vs/identifier-type',
        'value': '98736458',
        'period': {
            'start': '2014-02-30T00:00:00'
        },
        'assigner': 'AI'
    }],
    'name': [{
        'use': 'official',
        'text': 'John Doe',
        'family': 'Doe',
        'given': 'John'
    }],
    'telecom': [{
        'system': 'phone',
        'value': '(000) 867-5309',
        'use': 'home'
    }],
    'gender': 'male',
    'birthDate': '1950-05-14',
    'deceasedBoolean': False,
    'address': [{
        'use': 'home',
        'text': '1337 Hacker Way, 1st ST NY NY 10001',
        'line': '1337 Hacker Way',
        'city': 'New York', 
        'state': 'NY',
        'postalCode': '10001',
        'country': 'USA',
        'period': {
            'start': '2014-02-30T00:00:00'
        }
    }],
    'martialStatus': {
        'coding': {
            'system': 'http://hl7.org/fhir/v3/MaritalStatus/',
            'code': 'M',
        },
        'text': 'Married'
    },
    'multipleBirth': False,
    'contact': [{
        'relationship': {
            'coding': {
                'system': 'http://hl7.org/fhir/vs/patient-contact-relationship',
                'code': 'emergency'
            },
            'text': 'Emergency'
        },
        'name': [{
            'use': 'official',
            'text': 'Jane Doe',
            'family': 'Doe',
            'given': 'Jane'
        }],
        'gender': 'female',
        'address': [{
            'use': 'home',
            'text': '1337 Hacker Way, 1st ST NY NY 10001',
            'line': '1337 Hacker Way',
            'city': 'New York', 
            'state': 'NY',
            'postalCode': '10001',
            'country': 'USA',
            'period': {
                'start': '2014-02-30T00:00:00'
            }
        }],
        'period': {
            'start': '2014-02-30T00:00:00'
        },
        'telecom': [{
            'system': 'phone',
            'value': '(000) 867-5309',
            'use': 'home'
        }],
    }],
    'active': True
}