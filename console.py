import cmd

from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    prompt = " (hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("\n")
        return True
    # def help_exit(self):
        # print ("Exit the interpreter.")

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def do_create(self, arg):
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        try:
            args = []
            args = arg.split(" ")
            print(args[0])
            storage_dict = models.storage.all()
            key_to_delete = "{}.{}".format(args[0], args[1])
            if key_to_delete in storage_dict:
                del storage_dict[key_to_delete]
                models.storage.save()
        except KeyError:
            print("** class name missing **")
        except NameError:
            print("** class name missing **")

    def do_all(self, arg):
        listall = []
        storage_dict = models.storage.all()
        for k, v in storage_dict.items():
            listall.append(v)
        for o in listall:
            print(str(o))
            print(listall)

    def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found *")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        try:
            args = arg.split()
            if not args:
                print("** class name missing **")
                return

            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            instances = models.storage.all()
            instance_id = args[1]
            key = class_name + "." + instance_id
            attr_name = args[2]
            attr_value = args[3]
            if str(attr_value) is True:
                attr_value = attr_value[1:-1]
            try:
                attr_value = int(attr_value)
            except ValueError:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
            instance = instances[key]
            setattr(instance, attr_name, attr_value)
            instance.save()
        except IndexError:
            if len(args) < 2:
                print("** instance id missing **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
