def instances_counter(cls):
    cls.created_instances = 0
    
    def new_init(*args, **kwargs):
        cls.created_instances += 1
        return cls.__init_original__(*args, **kwargs)
    
    cls.__init_original__ = cls.__init__
    cls.__init__ = new_init
    
    def get_created_instances(self):
        return cls.created_instances
    
    def reset_instances_counter(self):
        result = cls.created_instances
        cls.created_instances = 0
        return result
    
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    
    return cls


@instances_counter 
class User: 
    pass
 
 
if __name__ == '__main__': 
    print(User.get_created_instances())  # 0 
    user, _, _ = User(), User(), User() 
    print(user.get_created_instances())  # 3 
    print(user.reset_instances_counter())  # 3