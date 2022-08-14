from app import HenseiTool
from static_data_manager import StaticDataManager
from hensei_data_manager import HenseiDataManager
from status_manager import StatusManager


def main():
    print("calling main")
    StaticDataManager()
    HenseiDataManager()
    StatusManager()
    app = HenseiTool()
    app.MainLoop()
    print("called main")


if __name__ == "__main__":
    main()
