using System.Windows;

namespace Twilight_Gatekeeper
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DatabaseHelper.InitializeDatabase();
        }

        private void AddUrlButton_Click(object sender, RoutedEventArgs e)
        {
            string url = UrlInput.Text;
            if (!string.IsNullOrWhiteSpace(url))
            {
                BlockedUrlsList.Items.Add(url);
                DatabaseHelper.SaveUrl(url);
                BlockUrl(url);
            }
            UrlInput.Clear();
        }

        public static void BlockUrl(string url)
        {
            string hostsPath = @"C:\Windows\System32\drivers\etc\hosts";
            string redirectEntry = $"127.0.0.1 {url}";

            if (!System.IO.File.ReadAllText(hostsPath).Contains(redirectEntry))
            {
                System.IO.File.AppendAllText(hostsPath, redirectEntry + System.Environment.NewLine);
            }
        }

        private void OpenStatisticsButton_Click(object sender, RoutedEventArgs e)
        {
            var statisticsPage = new StatisticsPage(); // Создаём страницу StatisticsPage
            this.Content = statisticsPage; // Устанавливаем содержимое окна на StatisticsPage
        }
    }
}
