using System.Windows;
using System.Windows.Controls;

namespace Twilight_Gatekeeper
{
    public partial class SettingsPage : Page
    {
        public SettingsPage()
        {
            InitializeComponent();
        }

        private void ChangePasswordButton_Click(object sender, RoutedEventArgs e)
        {
            string newPassword = NewPasswordBox.Password;

            if (!string.IsNullOrWhiteSpace(newPassword))
            {
                DatabaseHelper.SavePassword(newPassword);
                MessageBox.Show("Password changed successfully!");
            }
            else
            {
                MessageBox.Show("Password cannot be empty.");
            }
        }
    }
}
