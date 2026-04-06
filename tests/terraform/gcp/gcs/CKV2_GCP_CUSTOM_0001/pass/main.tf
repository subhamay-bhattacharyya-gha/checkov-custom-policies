resource "google_storage_bucket" "pass" {
  name                        = "compliant-bucket"
  location                    = "US"
  uniform_bucket_level_access = true
}
