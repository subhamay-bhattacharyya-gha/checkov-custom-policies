resource "google_storage_bucket" "fail" {
  name                        = "noncompliant-bucket"
  location                    = "US"
  uniform_bucket_level_access = false
}
