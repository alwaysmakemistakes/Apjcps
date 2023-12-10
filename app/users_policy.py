
# from flask_login import current_user

# class UsersPolicy:
#     def __init__(self, record):
#         self.record = record

#     def create(self):
#         return current_user.is_admin()

#     def delete(self):
#         return current_user.is_admin()

#     def show(self):
#         return True
    
#     def edit(self):
#         if current_user.id == self.record.id:
#             return True
#         return current_user.is_admin()

#     def change_role(self):
#         return current_user.is_admin()


from flask_login import current_user

class UsersPolicy:
    def __init__(self, record):
        self.record = record

    def create(self):
        return current_user.is_admin()

    def delete(self):
        return current_user.is_admin()

    def show(self):
        return True
    
    def edit_plastinka(self):
        return current_user.is_admin() or current_user.is_moder()
    
    def get_logs(self):
        return current_user.is_admin()

    def list_users(self):
        return current_user.is_admin() 
    
    def view_user(self):
        return current_user.is_admin() 
    
    def update_admin(self):
        return current_user.is_admin() 

        
    # def edit(self):
    #     if current_user.id == self.record.id:
    #         return True
    #     return current_user.is_admin() or current_user.is_moder()

