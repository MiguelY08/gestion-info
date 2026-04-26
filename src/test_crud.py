"""Test the new CRUD functions"""

import os
from service import ClientService

def main():
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')

    print("\n" + "="*60)
    print("🧪 TESTING NEW CRUD FUNCTIONS")
    print("="*60)

    service = ClientService(data_file)

    # Test list_records
    print("\n📋 LIST RECORDS:")
    service.list_records()

    # Test search_record
    print("\n🔍 SEARCH RECORD (ID 2):")
    service.search_record(2)

    print("\n🔍 SEARCH RECORD (ID 999 - not exists):")
    service.search_record(999)

    # Test new_register
    print("\n➕ NEW REGISTER:")
    service.new_register(4, "Ana Ruiz", "ana@email.com")

    # Test update_record
    print("\n✏️  UPDATE RECORD (ID 4):")
    service.update_record(4, name="Ana Ruiz Updated", email="ana.updated@email.com")

    # Test delete_record
    print("\n🗑️  DELETE RECORD (ID 4):")
    service.delete_record(4)

    # Test error cases
    print("\n❌ ERROR CASES:")
    service.new_register(1, "Duplicate", "dup@email.com")  # ID exists
    service.update_record(999, name="Not exists")  # ID not exists
    service.delete_record(999)  # ID not exists

    print("\n✅ CRUD tests completed")

if __name__ == "__main__":
    main()