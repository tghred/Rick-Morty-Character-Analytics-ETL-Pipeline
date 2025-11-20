

# Rick & Morty Character Analytics ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-green)
![License](https://img.shields.io/badge/License-MIT-green)
![ETL](https://img.shields.io/badge/Process-ETL-orange)

A professional ETL (Extract, Transform, Load) pipeline for collecting, processing, and analyzing character data from the Rick and Morty API. This system provides a robust foundation for data extraction and analysis with production-ready features including PostgreSQL integration.

## 🌟 Overview

An integrated system for extracting and analyzing Rick and Morty character data using ETL technologies. The system represents an automated platform for collecting data from public APIs, processing it, and storing it in multiple formats (JSON, CSV, PostgreSQL) to enable comprehensive analysis operations.

## 🚀 Features

### 🔄 Integrated ETL Process
- **Extraction**: Secure and reliable data retrieval from Rick and Morty API
- **Transformation**: Data cleaning, enrichment, and preparation for analysis
- **Load**: Data storage in multiple formats (JSON, CSV, PostgreSQL)

### 🗄️ Database Integration
- **PostgreSQL Support**: Full database integration with connection management
- **Configurable Settings**: Secure database configuration using INI files
- **Connection Pooling**: Robust connection handling with error recovery

### 🏗️ Scalable Architecture
- Modular design allowing easy integration of new data sources
- Multi-format storage support with database expansion capability
- Comprehensive error handling ensuring operational continuity

### ⚡ Enhanced Performance
- Intelligent request management respecting server limitations
- Parallel data processing across multiple pages
- Request rate control preventing blocking and ensuring stability

## 📦 Installation

### Prerequisites
- Python 3.7+
- PostgreSQL 12+
- pip package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/rick-morty-etl.git
cd rick-morty-etl

# Install dependencies
pip install -r requirements.txt
```

### Database Setup
1. Install PostgreSQL and create a database
2. Update the `database.ini` file with your credentials:
```ini
[postgresql]
host=localhost
database=postgres
user=postgres
password=44tt44ttaaSS
port=5432
connect_timeout=10
```

## 🛠️ Project Structure

```
rick-morty-etl/
├── src/
│   ├── __init__.py
│   ├── etl_pipeline.py          # Main ETL pipeline
│   ├── database/
│   │   ├── __init__.py
│   │   ├── config.py            # Database configuration
│   │   └── connection.py        # Database connection manager
│   └── utils/
│       ├── __init__.py
│       ├── data_processor.py    # Data transformation functions
│       └── file_exporter.py     # JSON/CSV export functions
├── config/
│   └── database.ini            # Database configuration
├── tests/
│   ├── test_etl.py
│   └── test_database.py
├── requirements.txt
├── README.md
└── examples/
    ├── basic_usage.py
    └── advanced_analysis.py
```

## 📋 Usage

### Basic Usage
```python
from src.etl_pipeline import main_etl_pipeline

# Run complete ETL pipeline
main_etl_pipeline()
```

### Advanced Usage with Custom Configuration
```python
from src.database.connection import db_connection
from src.etl_pipeline import get_all_characters, save_to_postgresql

# Custom ETL process
characters = get_all_characters()

# Save to PostgreSQL with custom settings
with db_connection(section='production') as conn:
    save_to_postgresql(characters, connection=conn)

# Export to files
from src.utils.file_exporter import save_to_json, save_to_csv
save_to_json(characters, 'output/characters.json')
save_to_csv(characters, 'output/characters.csv')
```

### Database Operations
```python
from src.database.connection import db_connection
from src.database.config import test_connection

# Test database connection
test_connection()

# Execute custom queries
with db_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM characters")
        count = cursor.fetchone()[0]
        print(f"Total characters: {count}")
```

## 🗃️ Database Schema

### Characters Table
```sql
CREATE TABLE characters (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50),
    species VARCHAR(100),
    episode_count INTEGER,
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Useful Queries
```sql
-- Character statistics by status
SELECT status, COUNT(*) as count 
FROM characters 
GROUP BY status 
ORDER BY count DESC;

-- Top characters by episode appearance
SELECT name, episode_count 
FROM characters 
ORDER BY episode_count DESC 
LIMIT 10;

-- Species distribution
SELECT species, COUNT(*) as count 
FROM characters 
GROUP BY species 
ORDER BY count DESC;
```

## ⚙️ Configuration

### Database Configuration
Create `config/database.ini`:
```ini
[postgresql]
host=localhost
database=postgres
user=postgres
password=44tt44ttaaSS
port=5432
connect_timeout=10

[production]
host=production-db.example.com
database=rick_morty_prod
user=app_user
password=prod_password
port=5432
```

### Environment Variables (Optional)
```bash
export DB_HOST=localhost
export DB_NAME=rick_morty_db
export DB_USER=postgres
export DB_PASSWORD=your_password
```

## 🧪 Testing

### Run Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/test_etl.py -v

# Run with coverage
python -m pytest --cov=src tests/
```

### Test Database Connection
```python
from src.database.connection import test_connection

# Test connection to default database
test_connection()

# Test connection to specific section
test_connection(section='production')
```

## 🐛 Error Handling

The system includes comprehensive error handling for:
- Network connectivity issues
- API rate limiting
- Database connection failures
- Data parsing errors
- File I/O operations

### Example Error Recovery
```python
try:
    with db_connection() as conn:
        # Database operations
        pass
except psycopg2.OperationalError as e:
    print(f"Database connection failed: {e}")
    # Implement retry logic or fallback
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 📊 Output Examples

### JSON Output
```json
[
  {
    "id": 1,
    "name": "Rick Sanchez",
    "status": "Alive",
    "species": "Human",
    "episode_count": 51,
    "location": "Earth"
  }
]
```

### CSV Output
```
id,name,status,species,episode_count,location
1,Rick Sanchez,Alive,Human,51,Earth
2,Morty Smith,Alive,Human,39,Earth
```

## 🔧 Development

### Adding New Data Sources
1. Create new extractor in `src/extractors/`
2. Implement transformation logic in `src/utils/data_processor.py`
3. Update database schema if needed
4. Add tests in `tests/`

### Code Style
```bash
# Format code
black src/ tests/

# Check code style
flake8 src/ tests/

# Type checking
mypy src/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Rick and Morty API](https://rickandmortyapi.com/) for providing the data
- PostgreSQL community for excellent database support
- Python community for robust data processing libraries

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/yourusername/rick-morty-etl/issues)
- Check the [examples](examples/) directory
- Review the [documentation](docs/)

## 🔮 Future Enhanceances

- [ ] Real-time data streaming
- [ ] Docker containerization
- [ ] REST API for data access
- [ ] Dashboard for visualization
- [ ] Machine learning integration

---

<div align="center">

**⭐ If you find this project useful, please give it a star! ⭐**

</div>
