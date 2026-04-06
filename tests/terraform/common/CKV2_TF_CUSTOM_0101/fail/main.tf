resource "null_resource" "fail" {
  provisioner "local-exec" {
    command = "echo 'running local commands'"
  }
}
