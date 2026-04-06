resource "google_storage_bucket" "pass" {
  name                     = "private-bucket"
  location                 = "US"
  public_access_prevention = "enforced"
}
