def check_access_bitwise(user_permissions: set, required_permissions: set) -> bool:
    # Set operation: check if all required permissions are a subset of user permissions
    has_permission = required_permissions.issubset(user_permissions)
    return has_permission

# Usage
user_perms = {"read", "write", "execute"}
req_perms = {"read", "write"}

print(check_access_bitwise(user_perms, req_perms))  # Returns True
