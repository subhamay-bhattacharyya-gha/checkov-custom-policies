resource "null_resource" "pass" {
  triggers = {
    value = "example"
  }
}
