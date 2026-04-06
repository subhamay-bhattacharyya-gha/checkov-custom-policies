resource "google_storage_bucket" "fail" {
  name     = "unversioned-bucket"
  location = "US"

  versioning {
    enabled = false
  }
}
