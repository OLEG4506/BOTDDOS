from kutana import Kutana, VKController, load_plugins, load_configuration


# Create engine
kutana = Kutana()

# Create VKController
kutana.add_controller(
    VKController(token = "d6842a32a19fefc24f1ac19b17cba1c9243f4bf1ecdf426215d193d96135a111d0d537f6e2df8f1452482")
)

# Load and register plugins
kutana.executor.register_plugins(*load_plugins("/root/bot/example/"))

# Run engine
kutana.run()
