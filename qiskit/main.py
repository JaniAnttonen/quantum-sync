from flask import Flask, request

from qiskit import IBMQ, QuantumCircuit, execute

app = Flask(__name__)

# Load your IBM Q account
IBMQ.load_account()

# Get the provider and backend
provider = IBMQ.get_provider(hub="ibm-q")
backend = provider.get_backend("your_backend_name")


@app.route("/execute", methods=["POST"])
def execute_quantum_circuit():
    # Get the quantum circuit from the request
    circuit = request.json.get("circuit")

    # Create a QuantumCircuit object
    qc = QuantumCircuit.from_qasm_str(circuit)

    # Execute the circuit on the backend
    job = execute(qc, backend)

    # Get the result
    result = job.result()

    # Return the result as JSON
    return result.to_dict()


if __name__ == "__main__":
    app.run()
