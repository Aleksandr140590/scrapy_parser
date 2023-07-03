import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = {}
        self.result_dir = BASE_DIR / 'results'
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        if item['status'] not in self.statuses:
            self.statuses[item['status']] = 1
        else:
            self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = 'status_summary_{}.csv'.format(
            datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        )
        csv_path = self.result_dir / filename
        rows = []
        for status, counter in self.statuses.items():
            rows.append([status,counter])
        with open(csv_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            writer = csv.writer(f)
            writer.writerows(rows)
            f.write(f'Total,{sum(self.statuses.values())}\n')
