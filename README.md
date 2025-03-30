# Data Processing Pipeline Using Kafka

## Project Overview
This project builds a **real-time data processing pipeline** using **Apache Kafka** and **Neo4j**. The pipeline ingests, processes, and analyzes data streams, ensuring efficient data flow and storage.

## Key Features
- **Apache Kafka Integration**: Manages real-time streaming data.
- **Neo4j Database**: Stores and analyzes graph-based data.
- **Automated Data Ingestion**: Uses Python scripts to load and process data.
- **Configuration via YAML**: Streamlines Kafka and Neo4j setup.

## Project Structure
```
Data-Processing-Pipeline-using-Kafka/
│── Project-Portfolio.pdf        # Detailed step-by-step project documentation
│── README.md                    # Project documentation
│── data_loader.py               # Loads data into Kafka topics
│── interface.py                  # Handles interactions between Kafka and Neo4j
│── tester.py                     # Validates data ingestion and processing
│── kafka-neo4j-connector.yaml    # Kafka-Neo4j integration settings
│── kafka-setup.yaml              # Kafka cluster configuration
│── neo4j-values.yaml             # Neo4j database configuration
│── zookeeper-setup.yaml          # Zookeeper setup for Kafka
```

## Installation & Setup
### Prerequisites
1. Install **Apache Kafka** and **Zookeeper**:
   - Follow instructions in `kafka-setup.yaml` and `zookeeper-setup.yaml`.

2. Install **Neo4j**:
   - Use `neo4j-values.yaml` for database configuration.

3. Install required Python dependencies:
   ```sh
   pip install kafka-python neo4j
   ```

### Running the Pipeline
1. **Start Kafka and Zookeeper**:
   ```sh
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties
   ```

2. **Run the Kafka-Neo4j connector**:
   ```sh
   python interface.py
   ```

3. **Load data into Kafka**:
   ```sh
   python data_loader.py
   ```

4. **Test the pipeline**:
   ```sh
   python tester.py
   ```

## Data Flow Overview
1. **Kafka Producers** (`data_loader.py`):
   - Reads data and sends it to Kafka topics.

2. **Kafka Consumers** (`interface.py`):
   - Listens to Kafka topics and processes the data.

3. **Neo4j Storage**:
   - The processed data is stored in Neo4j for analysis.

## Configuration Details
- Modify `kafka-neo4j-connector.yaml` to adjust how data flows between Kafka and Neo4j.
- Adjust `kafka-setup.yaml` for Kafka cluster configurations.
- Update `neo4j-values.yaml` to optimize the database.

## Testing
- `tester.py` verifies data ingestion and processing integrity.

## License
This project is open-source under the **MIT License**.
