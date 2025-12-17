"""
Rick & Morty ETL Pipeline - Main Entry Point
"""
import sys
import os

# Add the 'src' directory to Python's module search path
current_dir = os.path.dirname(__file__)
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)


def main():
    # Import here to avoid errors if path is not set
    from src.etl_pipeline import main_etl_pipeline
    from src.database.connection import test_connection

    print("🚀 Rick & Morty ETL Pipeline")
    print("=" * 40)

    print("🔌 Testing database connection...")
    if test_connection():
        print("✅ Database connection successful")
    else:
        print("❌ Database connection failed")
        return

    print("\n🔄 Running ETL pipeline...")
    main_etl_pipeline()
    print("\n🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()