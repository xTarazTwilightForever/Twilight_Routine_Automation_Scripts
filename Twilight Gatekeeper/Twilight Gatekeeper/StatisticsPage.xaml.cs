using System.Data;
using System.Data.SQLite;
using System.Windows.Controls;

namespace Twilight_Gatekeeper
{
    public partial class StatisticsPage : Page
    {
        public StatisticsPage()
        {
            InitializeComponent();
            LoadStatistics();
        }

        private void LoadStatistics()
        {
            using (var connection = new SQLiteConnection("Data Source=blocked_urls.db"))
            {
                connection.Open();
                string query = "SELECT Url, DateTime, Duration FROM Statistics";
                SQLiteDataAdapter adapter = new SQLiteDataAdapter(query, connection);
                DataTable dataTable = new DataTable();
                adapter.Fill(dataTable);

                StatisticsTable.ItemsSource = dataTable.DefaultView;
            }
        }
    }
}
