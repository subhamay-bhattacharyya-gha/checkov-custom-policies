resource "local_file" "pass" {
  content         = "example content"
  filename        = "/tmp/example.txt"
  file_permission = "0600"
}
