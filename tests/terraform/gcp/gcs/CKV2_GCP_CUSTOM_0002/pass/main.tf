resource "google_storage_bucket" "pass" {
  name     = "versioned-bucket"
  location = "US"

  versioning {
    enabled = true
  }
}
