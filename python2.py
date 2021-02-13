
namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string Eposta = textBox1.Text.Trim();

            var emailList = Eposta.Split('@');

           var returnValue = EmailIsValid(emailList);

            if (returnValue == true)
                MessageBox.Show("Email Dogru!");
            else
                MessageBox.Show("Email Yanlıs!");
        }

        public bool EmailIsValid(string[] emailList)
        {
            bool EmailValid = false;

            var KullaniciAdiDogruMu = false;
            var uzantiDogruMu = false;

            if (emailList.Count() >= 2)
            {
                var kullaniciAdi = emailList[0];
                var uzanti = emailList[1];

                if (SayiHarfAltCizgiIcerirMi(kullaniciAdi) == true)
                {
                    KullaniciAdiDogruMu = true;
                }

                var uzantiSayisi = uzanti.Split('.').Count();

                if (uzantiSayisi >= 1 && uzantiSayisi <= 3)
                {
                    uzantiDogruMu = true;
                }

                if (KullaniciAdiDogruMu == true && uzantiDogruMu == true)
                    EmailValid = true;
            }
            else
            {
                EmailValid = false;
            }

           

            return EmailValid;
        }

        bool SayiHarfAltCizgiIcerirMi(string text)
        {
            foreach (char chr in text)
            {
                if (!Char.IsLetterOrDigit(chr) && chr != '-' && chr != '_') return false;
            }
            return true;
        }

    }
}
