resource "google_storage_bucket" "fail" {
  name     = "google-managed-key-bucket"
  location = "US"
}
