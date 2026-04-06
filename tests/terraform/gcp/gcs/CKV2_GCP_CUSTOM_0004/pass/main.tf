resource "google_storage_bucket" "pass" {
  name     = "cmek-encrypted-bucket"
  location = "US"

  encryption {
    default_kms_key_name = "projects/my-project/locations/us/keyRings/my-ring/cryptoKeys/my-key"
  }
}
