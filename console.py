import cmd

from models.base_model import BaseModel
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
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
