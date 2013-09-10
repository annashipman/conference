Vagrant.configure("2") do |config|
  config.vm.box = "conference_20130910"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"
  config.vm.hostname = "annashipman"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.provision :shell, :path => "provision.sh"
end
