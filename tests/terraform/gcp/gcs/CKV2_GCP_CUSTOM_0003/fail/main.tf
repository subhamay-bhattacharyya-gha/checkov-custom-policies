resource "google_storage_bucket" "fail" {
  name                     = "public-bucket"
  location                 = "US"
  public_access_prevention = "inherited"
}
