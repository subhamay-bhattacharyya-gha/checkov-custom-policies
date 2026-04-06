resource "local_file" "fail" {
  content         = "example content"
  filename        = "/tmp/example.txt"
  file_permission = "0644"
}
