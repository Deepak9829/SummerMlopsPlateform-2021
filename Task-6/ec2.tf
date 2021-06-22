provider "aws" {
	region = "ap-south-1"
	profile = "Deep"
}

resource "aws_instance" "os1" {
  ami           = "ami-06a0b4e3b7eb7a300"
  instance_type = "t2.micro"
  #count = 5

  tags = {
    Name = "Server"
  }
}


variable "osname" {
  type = string
  default = "RedHat"
}

output "out" {
  value = aws_instance.os1.public_ip

}
resource "aws_ebs_volume" "myExtraHDD" {

  availability_zone = aws_instance.os1.availability_zone
  size              = 1

  tags = {
    Name = "MyExtraHDD"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.myExtraHDD.id
  instance_id = aws_instance.os1.id
}