using System;
using System.Data.SQLite;
using System.Security.Cryptography;
using System.Text;

namespace Twilight_Gatekeeper
{
    public static class DatabaseHelper
    {
        private const string ConnectionString = "Data Source=blocked_urls.db";

        public static void InitializeDatabase()
        {
            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();

                // Таблица для хранения заблокированных URL
                string createBlockedUrlsTable = @"
                    CREATE TABLE IF NOT EXISTS BlockedUrls (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Url TEXT
                    )";
                SQLiteCommand blockedUrlsCommand = new SQLiteCommand(createBlockedUrlsTable, connection);
                blockedUrlsCommand.ExecuteNonQuery();

                // Таблица для хранения настроек (например, пароля)
                string createSettingsTable = @"
                    CREATE TABLE IF NOT EXISTS Settings (
                        Key TEXT PRIMARY KEY,
                        Value TEXT
                    )";
                SQLiteCommand settingsCommand = new SQLiteCommand(createSettingsTable, connection);
                settingsCommand.ExecuteNonQuery();
            }
        }

        public static void SaveUrl(string url)
        {
            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();
                string insertQuery = "INSERT INTO BlockedUrls (Url) VALUES (@Url)";
                SQLiteCommand command = new SQLiteCommand(insertQuery, connection);
                command.Parameters.AddWithValue("@Url", url);
                command.ExecuteNonQuery();
            }
        }

        public static void SavePassword(string password)
        {
            using (var connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();
                string hashedPassword = HashPassword(password); // Хэшируем пароль
                string insertQuery = "REPLACE INTO Settings (Key, Value) VALUES ('Password', @Password)";
                SQLiteCommand command = new SQLiteCommand(insertQuery, connection);
                command.Parameters.AddWithValue("@Password", hashedPassword);
                command.ExecuteNonQuery();
            }
        }

        private static string HashPassword(string password)
        {
            using (var sha256 = SHA256.Create())
            {
                byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
                return Convert.ToBase64String(bytes);
            }
        }
    }
}
