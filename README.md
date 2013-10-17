config
======

A python (2.6+/3+) configuration container with several access modes

The Configuration class is a dictionary container usable in several ways with key/value data.
You can get easily the configuration from a file.
You can use it like a dictionary. You can use getters and setters. You can use it like a class with variables.

Exemple:
--------

- myconfig.txt:

        # the name
        
        name = "Foo Bar"
        
        country = France # is beautiful
        
        comment = "#this is like a comment with a #!"


- configtest.py:

        #!/usr/bin/python
        from Configuration import Configuration
        c = Configuration("myconfig.txt", {"home": "Here", "text": "This is a test"})
        c.set_new_param("One more")
        c["other"] = "This is good!"
        print("The param home = " + c.home)
        print("The param name = " + c.name)
        print("The param country = " + c["country"])
        print("The param text = " + c.get_text())
        print("-------")
        for k in c:
            print(k + " = " + c[k])
        print("-------")
        print(str(c))
        print("-------")
        if 'new_param' in c:
            print("Found new_param")
        if 'old_param' not in c:
            print("Not found old_param")

- result of execution:

        The param home = Here
        The param name = Foo Bar
        The param country = France
        The param text = This is a test
        -------
        name = Foo Bar
        country = France
        new_param = One more
        other = This is good!
        home = Here
        text = This is a test
        -------
        name: Foo Bar
        country: France
        new_param: One more
        other: This is good!
        home: Here
        text: This is a test
        
        -------
        Found new_param
        Not found old_param

