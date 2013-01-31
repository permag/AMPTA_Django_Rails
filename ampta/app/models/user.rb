class User < ActiveRecord::Base
  attr_accessible :first_name, :last_name, :email, :password
  has_and_belongs_to_many :projects
  has_many :tickets
end
